#!/usr/bin/env bash
#
# Provision the Codespace: the jPipe compiler (plus its Java 25 / Graphviz runtime)
# and the pinned Python environment. Run once, by onCreateCommand.
set -euo pipefail

PYTHON_VERSION="3.13"   # the floor [requires] python_version sets in the Pipfile
JPIPE_VERSION="2.5.0"   # used only by the fallback install path below

log() { echo "[setup] $*"; }

# Fallback for step 2 - the release tarball ships jpipe.jar plus a launcher whose
# @@JAVA@@ and @@PREFIX@@ placeholders the packaging channel substitutes at install
# time. Both runtime dependencies are in the Ubuntu archive, so this needs no PPA.
install_jpipe_from_release() {
    local url="https://github.com/jpipe-mcscert/jpipe-compiler/releases/download/v${JPIPE_VERSION}/jpipe-${JPIPE_VERSION}.tar.gz"
    sudo apt-get install -y openjdk-25-jre-headless graphviz
    curl -fsSL "$url" | sudo tar xz -C /opt
    sudo sed -i "s|@@JAVA@@|$(command -v java)|; s|@@PREFIX@@|/opt/jpipe-${JPIPE_VERSION}|" \
        "/opt/jpipe-${JPIPE_VERSION}/jpipe"
    sudo ln -sf "/opt/jpipe-${JPIPE_VERSION}/jpipe" /usr/local/bin/jpipe
}

# Step 1 - package sources. Both PPAs are added with --no-update so the whole
#          setup refreshes the apt index once, not three times.
log "configuring package sources"
sudo apt-get update
sudo apt-get install -y software-properties-common
sudo add-apt-repository -y --no-update ppa:mcscert/ppa      # the jPipe compiler
sudo add-apt-repository -y --no-update ppa:deadsnakes/ppa   # Python 3.13; noble ships 3.12
sudo apt-get update

# Step 2 - jPipe compiler. Its .deb depends on openjdk-25-jre-headless and
#          graphviz, so apt pulls the native toolchain along with it.
log "installing the jPipe compiler"
if ! sudo apt-get install -y jpipe; then
    log "PPA install failed - falling back to the GitHub release tarball"
    install_jpipe_from_release
fi

# Step 3 - Python 3.13 from apt, rather than the devcontainer python feature:
#          that feature has no prebuilt binary for noble and compiles CPython
#          from source, which alone cost ~15 minutes of the build.
log "installing Python ${PYTHON_VERSION}"
sudo apt-get install -y "python${PYTHON_VERSION}" "python${PYTHON_VERSION}-venv" pipx

# Step 4 - Python environment, exactly as pinned in the committed Pipfile.lock
#          (jpipe-runner, which executes the justification models).
log "installing the Python environment"
export PATH="${HOME}/.local/bin:${PATH}"
export PIPENV_VENV_IN_PROJECT=1
pipx install pipenv
pipenv sync --dev --python "/usr/bin/python${PYTHON_VERSION}"

# Step 5 - prove the toolchain in the creation log
log "verifying"
jpipe doctor
# jpipe-runner has no --version flag; its banner carries the version instead.
pipenv run jpipe-runner --help | grep -i 'Version'
log "ready"
