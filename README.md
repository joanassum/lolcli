# lolcli -- CLI for League of Legends
## Installation

1. Clone this repo.
2. Install dependencies. (For guide to use virtualenv, see [https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/]())
    ```
        pip3 install -r requirements.txt
    ```
3. Get API key from the League of Legends Developers Portal.
3. Add the following line to your .bashrc, replace the path with your own path (e.g. $HOME/quoty).
    ```
        export LOLCLI_APIKEY=<api-key>
        export LOLCLI_PATH=<path-to-lolcli>
        alias lolcli='python $LOLCLI_PATH/lolcli.py'
    ```
    For virtualenv, last line can be done as ```alias lolcli='f(){ source <path-to-virtualenv-activate>; python $LOLCLI_PATH/lolcli.py $@; deactivate;unset -f f;}; f'```

## Usage
`lolcli freechamp` will return all free to play champion rotation.
More Functionality to be added.