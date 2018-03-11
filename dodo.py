from pyct import *

# debugging
def tmp(task,values):
    print(os.path.join(sys.prefix,"envs",task.options['name']))
    print(os.path.exists(os.path.join(sys.prefix,"envs",task.options['name'])))
    return os.path.exists(os.path.join(sys.prefix,"envs",task.options['name']))

def task_create_env():
    python = {
        'name':'python',
        'long':'python',
        'type':str,
        'default':'3.6'}

    name = {
        'name':'name',
        'long':'name',
        'type':str,
        'default':'test-environment'}

    return {
        'params': [python,name],
        # TODO: this assumes env created in default location...but
        # apparently any conda has access to any other conda's
        # environments (?!) plus those in ~/.conda/envs (?!)
        'uptodate': [tmp],        
#        'uptodate': [lambda task,values: os.path.exists(os.path.join(sys.prefix,"envs",task.options['name']))],
        'actions': ["conda create -y --name %(name)s python=%(python)s"]}
