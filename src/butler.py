!#python

import os, logging

### Path where this script resides ###
def getScriptPath():
    return os.path.dirname(os.path.realpath(__file__))


### Get duties folder ###
def getDutiesPath():
    return os.path.join(getScriptPath(), 'duties')


### Get all the duties from the duties folder and filter non duties ###
def getDuties():
    raw = os.listdir(getDutiesPath())
    raw = dutyFilterToPythonFiles(raw)
    raw = dutyFilterAreNumberedFiles(raw)
    raw = dutyFilterIsProperDuty(raw)


### Filter out files that don't have the python file extension ###
def dutyFilterToPythonFiles(raw):
    return [x for x in raw if x.endswith('.py')]


### Filter out files that are not properly formatted, or missing is methods ###
def dutyFilterIsProperDuty(raw):
    # TODO can implement this later
    return [x for x in raw if dutyIsProper(x)]


### Helper method to check duty file and abstract to just yes/no ###
def dutyIsProper(f):
    results = {}
    results['simple'] = dutyIsProperSimple(f)
    results['success'] = dutyIsProperFull(f)
    return results['success']


### Full check of duty file ###
def dutyIsProperFull(f):
    return True


### Simple check of duty file ###
def dutyIsProperSimple(f):
    return True


### List comprehension to remove non-numbered directories from list ###
def dutyFilterAreNumberedFiles(raw):
    logging.debug("Weeding out non-numbered directories")
    logging.debug("Before: \n" + str(d))

    d = [x for x in d if x[0].isdigit()]

    logging.debug("After: \n" + str(d))
    return d


### Respond to call from command line ###
if __name__ == "__main__":
    global cwd
    cwd = os.getcwd()
    
    ### Arg Parsing ###
    # parser = argparse.ArgumentParser()
    # parser.add_argument('name', help='Name of the project (and folder) to create', nargs='?', default='_stop_')
    # parser.add_argument('-c', '--contributors', dest='contributors', help='Contributors to the project', nargs=3, action='append', metavar=('cName', 'cEmail', 'cRank'))
    # parser.add_argument('-d', '--directory', dest='directory', help='Custom directory location for new project')
    # parser.add_argument('-e', '--example', dest='example', help='Generate example folder', action='store_true')
    # parser.add_argument('-i', '--info', dest='info', help='Very short description of the project')
    # parser.add_argument('-s', '--scm', dest='scm', help='Which source control management you would like initialized', choices=['git', 'None'])
    # parser.add_argument('-t', '--template', dest='template', help="Template name (also used as the name of the template's enclosing folder)", default='Generic')
    # parser.add_argument('-v', '--verbose', dest='verbosity', help='Increase verbosity (off/on/firehose)', action='count', default=0)
    # args = parser.parse_args()
    
    # ### Initialize Logging ###
    # if args.verbosity == 0:
    #     l = logging.WARNING
    # elif args.verbosity == 1:
    #     l = logging.INFO
    # else:
    #     l = logging.DEBUG
        
    # TODO uncomment this
    # logging.basicConfig(level=l, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    
    # if ((args.name == '_stop_') or args.example):
    #     ### Generate Example Project/Folder ###
    #     genExampleFolder()
    # else:
    #     ### Generate Project/Folder ###
        
    #     os.chdir(cwd)
        
    #     # Set arguments with default options
    #     o = genDefaultOptions();
    #     logging.debug('Defaults: ' + str(o))
    #     logging.debug('Args: ' + str(args))

    #     o['name'] = args.name # This will either be true, or get a default value that won't reach this point
    #     o['contributors'] = o['contributors'] if getattr(args, 'contributors') is None else args.contributors
    #     o['directory'] = o['directory'] if getattr(args, 'directory', o['directory']) is None else args.directory
    #     o['example'] = args.example # This always gets either true or false, no need for default here
    #     o['info'] = o['info'] if getattr(args, 'info') is None else args.info

    #     # TODO might need to catch an except here..
    #     scmtmp = getattr(args, 'scm', o['scm'])
    #     if scmtmp is None:
    #         o['scm'] = '_stop_'
    #     elif scmtmp == 'None':
    #         o['scm'] = '_stop_'
    #     else:
    #         o['scm'] = args.scm

    #     o['template_name'] = o['template_name'] if getattr(args, 'template') is None else args.template
    #     logging.info('Args with Defaults: ' + str(o))

    #     # Call Project Creation
    #     create_project(o)
        
    ### Reset working directory to original ###
    os.chdir(cwd)
