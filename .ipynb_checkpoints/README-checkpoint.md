
## After creating the working folder,

1. create virtual env
    $ python3 -m venv VirtualEnv(creating virtual env of your own)
    - 'VirtualEnv' is just  arbitrary name

2. activate env
    $ source VirtualEnv/bin/activate
    
3. install
    $ pip3 install matplotlib numpy pylzma ipykernel jupyter
    - pylzma will complain alot (c++ related error, i guess)

4. install 
    $ pip3 install torch torchvision torchaudio

5. create the kernel
    $ python3 -m ipykernel install --user --name=gpu_kernel --display-name "gpu kernel"

6. to call the jupyter notebook,
    $ jupyter notebook
