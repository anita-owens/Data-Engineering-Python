import os

def env_vars(request):
    ##ENVIRONMENT VARIABLES
    
    # Returns the environment variable to the console: $foo
    return os.environ.get('FOO', 'Specified environment variable is not set.') 
    
    # Returns the environment variable to the console: $anita
    return os.environ.get('NAME') 

    #Just prints $OK to the console - prints value of variable in the log:  anita
    name = os.environ.get('NAME')
    print(name) 

    ## SECRET MANAGER - EXPOSED AS ENVIRONMENT VARIABLE
    
    #Gets the secret from secret mgr and prints OK to the console when executed - does not print the secret value to the console or the log
    return os.environ.get('my-secret')

    return os.environ.get('server')
    server_pw = os.environ.get('server')
    my_secret_pw = os.environ.get('my-secret')

    ## SECRET MANAGER - Mounted as a volume
    
    #Gets the secret from secret mgr and prints $OK to the console - does not print the secret value to console or the logs. Text Payload: Function execution took 131 ms, finished with status code: 200"
    return os.environ.get('my-name') 

    #Gets the secret from secret mgr and prints OK to the console - does not print the secret value to the logs
    print(os.environ.get('my-name')) 
