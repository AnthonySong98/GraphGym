#!/bin/bash

if [ $TRAVIS_OS_NAME = 'osx' ]; then

    # Install some custom requirements on macOS
    # e.g. brew install pyenv-virtualenv

    case "${IDX}" in
        cpu)
            pip -q install torch torchvision torchaudio
            ;;
    esac
fi

if [ $TRAVIS_OS_NAME = 'linux' ]; then
    # Install some custom requirements on Linux
    case "${IDX}" in
        cu102)
            pip -q install torch torchvision torchaudio
            ;;
        
        cu111 | cpu)
            pip install -q torch==${TORCH_VERSION}+${IDX} torchvision==${TORCHVISION_VERSION}+${IDX} torchaudio==0.8.0 -f https://download.pytorch.org/whl/torch_stable.html
            ;;

        *)
            # may fail
            pip install -q torch==${TORCH_VERSION}+${IDX} torchvision==${TORCHVISION_VERSION}+${IDX} torchaudio==0.8.0 -f https://download.pytorch.org/whl/torch_stable.html
            ;;
    esac
fi

if [ $TRAVIS_OS_NAME = 'windows' ]; then
    # Install some custom requirements on windows
    case "${IDX}" in
        cu102 | cu111 | cpu)
            pip install -q torch==${TORCH_VERSION}+${IDX} torchvision==${TORCHVISION_VERSION}+${IDX} torchaudio==0.8.0 -f https://download.pytorch.org/whl/torch_stable.html
            ;;
            
        *)
            # may fail
            pip install -q torch==${TORCH_VERSION}+${IDX} torchvision==${TORCHVISION_VERSION}+${IDX} torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
            ;;
    esac
fi