<<<<<<< HEAD
# pathfinder177_platform
homework-2

task-1
1) ������ ServiceAccount bob � ������ ���������
2) ������ ClusterRoleBinding �� ������ ClusterRole admin ��� subject bob �� ������ ���������

task-2
1) ������ namespace prometheus � ������ ���������
2) ������ service account carol �� ������ ���������
3) ������ ClusterRole pod-reader � verbs get, list,watch � ������� ���������
4) ������ Rolebinding ��� subject groups, 
� ������� ��������� system:serviceaccounts:prometheus ���
������������� ���� pod-reader ���� serviceaccounts � �������� namespace prometheus � ��������� ���������

task-3
1) ������ namespace dev
2) ������ serviceaccount jane � namespace dev
3) ������ Rolebinding ��� ������������� jane ���� admin � namespace dev
4) ������ serviceaccount ken � namespace dev
5) ������ Rolebinding ��� ������������� ken ���� view � namespace dev
=======
hw-5
Branch kubernetes-storage

Задача - подготовка инфраструктуры

SINodeInfo feature gate must be enabled.
enable the VolumeSnapshotDataSource
Включить defaultstorageclass

0)Установить csi-driver-host-path
https://github.com/kubernetes-csi/csi-driver-host-path
1) Создать hostpath CSI storage class
2) Создать hostpath CSI PVC(существующий PV тоже можно использовать)
3) Создать pod с hostpath CSI PVC
4) Включить необходимые плагины для создания snapshots:
defaultStorageClass
VolumeSnapshotDataSource(alpha)
5) Описать объект типо VolumeSnapshot(при указании стандартного класса csi-hostpath-snapclass объект VolumeSnashotClass можно не создавать)

sCN in PV = sCN in PVC
>>>>>>> 842117d1342c8b55ba959a84729b76fa46716365
