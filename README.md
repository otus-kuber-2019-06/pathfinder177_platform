hw-5
Branch kubernetes-storage

Задача - подготовка инфраструктуры

Как установить csi driver
dynamic provisioning?
volume snapshot class?

SINodeInfo feature gate must be enabled.
enable the VolumeSnapshotDataSource
Включить defaultstorageclass
Включить снапшоты(это альфа)
1) Создать pod с описанием pv hostpath
2) Создать pv, host-path, описать storage-class
HP - прокидывание директории /data в контейнер
3) Создание pvc
4) Создать Storage class для CSI HPD
5) В cluster описать VolumeSnapshotContent из pvc(csi-hpd), специфицировать snapshot-class-name для hpd

sCN in PV = sCN in PVC
