import apt
from apt_deps.get_deps import DepFinder
import argparse

parser = argparse.ArgumentParser("Package Manager")
parser.add_argument("package", help="Package name you want to search", type=str)
parser.add_argument("-c","--count", help="number of packages installed on the system", action="store_true", default=False)
parser.add_argument("-o","--output", help="Allows display of outputs", action="store_false", default=True)

#main process
_cache = apt.Cache()
packages = [pack.name for pack in _cache]

def numOfPackage():
    return str(len(packages))


def isAvailablePackage(pack_name):
    return True if (pack_name in (pkg.name for pkg in _cache if pkg.is_installed)) else False

def package_controller(pack_name):

    installed_dep_package = list()
    not_installed_dep_package = list()

    try:
        deps = DepFinder(['apt',pack_name])
    except:
        print('There is no such package !!\nPlease enter an existing package name.')
        return

    if not isAvailablePackage(pack_name):
        print(f'The package is not installed ! : {pack_name}')
        print(f'There are {len(list(deps.dep_set))} dependencies of the {pack_name} package')
        
        for item in list(deps.dep_set):
            if isAvailablePackage(item):
                installed_dep_package.append(item)
            else:
                not_installed_dep_package.append(item)
        print('\n\tINSTALLED PACKAGE ON THE SYSYEM\n\t------------------------------')
        [print('\tPACKAGE NAME : ', ip) for ip in installed_dep_package]
        print('\n\n\tNOT INSTALLED PACKAGE ON THE SYSYEM\n\t----------------------------------')
        [print('\tPACKAGE NAME : ', ip) for ip in not_installed_dep_package]
        print('\n\n******************************************************\n')
        print(f'{len(not_installed_dep_package)} dependencies need to be installed ...\nOK...\n\n')
        

    else:
        print('The packet installed on the system ...')

if __name__ == '__main__':

    args = parser.parse_args()
    if args.count:
        print("\nNumber of the package on this system : ", numOfPackage(),"\n")
    if args.output:
        package_controller(args.package)
        


