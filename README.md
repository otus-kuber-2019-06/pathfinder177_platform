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