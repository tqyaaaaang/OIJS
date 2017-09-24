#!/bin/bash

# OIJS: install.sh

set -e;   # Exit if any command fails

current_mode=;



# functions

install ()
{
	if [ $current_mode == "root" ]; then
		sudo -H pip3 install .
	else
		pip3 install .
	fi

    return 0;
}

uninstall ()
{
	if [ $current_mode == "root" ]; then
		sudo -H pip3 uninstall -y oijs
	else
		pip3 uninstall -y oijs
	fi

    return 0;
}

upgrade ()
{
	if [ $current_mode == "root" ]; then
		sudo -H pip3 install --upgrade .
	else
		pip3 install --upgrade .
	fi

    return 0;
}



# main

if [ "$(whoami)" == "root" ]; then
	current_mode="root";
else
	current_mode="normal";
fi

if [ $# == 1 ]; then
    case $1 in
        install )
            install;;
        uninstall )
            uninstall;;
        upgrade )
            upgrade;;
        * )
            echo "Unknown Argument!";
            echo "Read the documents for more information."
            exit -1;;
    esac
else
    echo "Unknown Argument!";
    echo "Read the documents for more information."
    exit -1;
fi
