# PACKAGE QUERYING

HAVELSAN Pardus - Liman Teknoloji Kampı boyunca geliştirmiş olan paket ön sorgu aracı. Bu scriptin amacı; sistem üzerinde kurulu olan tüm paketlerin sayısını göremek, aramak istediğiniz paketin sistemde yüklü olup olmadığını kontrol etmek. Eğer aranan paket sistemde yüklü değil ise bağımlılıklarını görüntüleyebilir, hangilerinin yüklü olup olmadığını kolay bir şekilde görüntüleyebilirsiniz.
<br><br>

## ARAÇ BAĞIMLILIKLARI

    argparse
    apt_deps==1.2.1
    apt-py==0.0.1

<br>

## KULLANIM
<br>
Bu aracı kullanabilmek amacıyla ilk olarak yukarıda belirtilen bağımlılıkları yüklemeniz gerekecetir. Bunun için;
<br><br>


    sudo pip install -r requirements.txt
<br>
Paketleri başarılı bir şekilde yükledikten sonra aşağıdaki komut ile aracı çalıştırmış olunur:
<br><br>

    python3 PackageManager.py <package> -c -o

<br>

PARAMETRELER

*   package : Sistem üzerinde aranacak paketin ismi.
*   -c : Sistemdeki yüklü paket sayısını gösterilmesini sağlar.
*   -o : Paketin sistemde olmaması halinde çıktıyı engellemek için kullanılır. Genel olarak sadece paket sayısını yazdırmak için bu parametre girdisi verilir.

