To run this server, here are the steps:

1. Create python environment. Activate that environment, install the requirements
   - When install uwsgi, you might encounter errors:
       - need to install c compiler to build uwsgi error. Then just run `sudo apt install gcc`.
       - fatal error: Python.h: No such file or directory - Failed building wheel for uwsgi. If that's the case then you have to run `sudo apt install libpython3.8-dev` on your machine.
3. Run `uwsgi uwsgi.ini`. Uwsgi should be installed through pip in the previous step
4. `tail -f tower-server.log` to see the log as things happen



