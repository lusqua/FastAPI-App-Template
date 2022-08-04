

function venv_activate() {
    if [ -z "$VIRTUAL_ENV" ]; then
        echo "$(tput setaf 6)Activating virtual environment...$(tput sgr0)"
        source venv/bin/activate
    fi
}

function update_pip() {
    echo "$(tput setaf 6)Updating pip...$(tput sgr0)"
    pip install --upgrade pip
}

function install_pip_packages() {
    echo "$(tput setaf 6)Installing pip packages...$(tput sgr0)"
    pip install -r requirements.txt
}

function init() {
    echo "$(tput setaf 6)Initializing virtual environment...$(tput sgr0)"
    venv_activate
    update_pip
    install_pip_packages
}

if [ -d "venv" ]; then
    init
else
    echo "$(tput setaf 3)Venv not found. Creating..."
    if [ $(python -m venv venv 2> /dev/null ) ]; then
        echo "$(tput setaf 6)Venv created with python -m. Installing dependencies..."
    else
        echo "$(tput setaf 6)Venv created with python3 -m. Installing dependencies...."
        python3 -m venv venv
    fi
    init
fi

echo "$(tput setaf 2)SUCESS ENVIROMENT READY FOR USE.$(tput sgr0)"