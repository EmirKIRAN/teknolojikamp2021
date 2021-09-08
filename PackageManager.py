import apt
from apt_deps.get_deps import DepFinder
import argparse

# Kullanıcıdan alınacak parametreleri için argparse kullanıldı.
parser = argparse.ArgumentParser("Package Manager")
parser.add_argument("package", help="Package name you want to search", type=str)  # Aranacak paket ismini kullanıcıdan almak için argüman oluşturuldu.
parser.add_argument("-c","--count", help="number of packages installed on the system", action="store_true", default=False) # Sistemdeki yüklü paket sayısını yazdırmak için parametre
parser.add_argument("-o","--output", help="Allows display of outputs", action="store_false", default=True) # Paket çıktılarını gizlemek için parametre

#main process
# apt list verileri elde edilerek bir listeye yazılır.
_cache = apt.Cache()
packages = [pack.name for pack in _cache]

# Sistem üzerinde yüklü paket sayısını geri döner
def numOfPackage():
    return str(len(packages))


# Verilen kütüphanenin sistemde yüklü olup olmadığını kontrol eder.
def isAvailablePackage(pack_name):
    return True if (pack_name in (pkg.name for pkg in _cache if pkg.is_installed)) else False

# Paket ile ilgili kontrolleri yapan birim
def package_controller(pack_name):

    installed_dep_package = list() # İlgili paketin yüklenmiş olan bağımlılıklarını saklar.
    not_installed_dep_package = list() # İlgili paketin yüklenmemiş olan bağımlılıklarını saklar.

    try:
        deps = DepFinder(['apt',pack_name]) # Verilen paket ismine ait bağımlılıkları arar.
    except:
        print('There is no such package !!\nPlease enter an existing package name.') # Eğer verilen isimde bir paket yoksa hata mesajı ekrana yazılır.
        return

    if not isAvailablePackage(pack_name): # Eğer paket sistemde yüklü değil ise
        print(f'The package is not installed ! : {pack_name}') # Paketin yüklü olmadığı kullanıcıya bildirilir.
        print(f'There are {len(list(deps.dep_set))} dependencies of the {pack_name} package') # Pakete ait bağımlılıkların sayısı ekrana yazdırılır.
        
        for item in list(deps.dep_set): # İlgili dosyaya ait bağımlılıkların yüklü olup olmadığı kontrol edilir.
            if isAvailablePackage(item): # Eğer bağımlılık sistemde hali hazırda yüklü ise listeye eklenir.
                installed_dep_package.append(item)
            else:
                not_installed_dep_package.append(item)
        
        # Aşağıdaki alanda yüklü olan ve olmayan paket isimleri yazdırılır.
        print('\n\tINSTALLED PACKAGE ON THE SYSYEM\n\t------------------------------')
        [print('\tPACKAGE NAME : ', ip) for ip in installed_dep_package]
        print('\n\n\tNOT INSTALLED PACKAGE ON THE SYSYEM\n\t----------------------------------')
        [print('\tPACKAGE NAME : ', ip) for ip in not_installed_dep_package]
        print('\n\n******************************************************\n')
        print(f'{len(not_installed_dep_package)} dependencies need to be installed ...\nOK...\n\n')
        

    else:
        print('The packet installed on the system ...') # Verilen paket sistemde yüklü ise bilgilendirme mesajı ekrana yazdırılır.

if __name__ == '__main__':

    args = parser.parse_args()
    if args.count:
        print("\nNumber of the package on this system : ", numOfPackage(),"\n") # Sistem üzerindeki paket sayısı ekrana yazdırılır.
    if args.output:
        package_controller(args.package)
        


