<<<<<<< HEAD
# pathfinder177_platform
homework-2

task-1
1) Ñîçäàë ServiceAccount bob â ïåğâîì ìàíèôåñòå
2) Ñîçäàë ClusterRoleBinding íà îñíîâå ClusterRole admin äëÿ subject bob âî âòîğîì ìàíèôåñòå

task-2
1) Ñîçäàë namespace prometheus â ïåğâîì ìàíèôåñòå
2) Ñîçäàë service account carol âî âòîğîì ìàíèôåñòå
3) Ñîçäàë ClusterRole pod-reader ñ verbs get, list,watch â òğåòüåì ìàíèôåñòå
4) Ñîçäàë Rolebinding äëÿ subject groups, 
â êîòîğîì îïğåäåëèë system:serviceaccounts:prometheus äëÿ
äåëåãèğîâàíèÿ ğîëè pod-reader âñåì serviceaccounts â ïğåäåëàõ namespace prometheus â ÷åòâåğòîì ìàíèôåñòå

task-3
1) ñîçäàë namespace dev
2) ñîçäàë serviceaccount jane â namespace dev
3) Ñäåëàë Rolebinding äëÿ äåëåãèğîâàíèÿ jane ğîëè admin â namespace dev
4) ñîçäàë serviceaccount ken â namespace dev
5) Ñäåëàë Rolebinding äëÿ äåëåãèğîâàíèÿ ken ğîëè view â namespace dev
=======
hw-5
Branch kubernetes-storage

Ğ—Ğ°Ğ´Ğ°Ñ‡Ğ° - Ğ¿Ğ¾Ğ´Ğ³Ğ¾Ñ‚Ğ¾Ğ²ĞºĞ° Ğ¸Ğ½Ñ„Ñ€Ğ°ÑÑ‚Ñ€ÑƒĞºÑ‚ÑƒÑ€Ñ‹

SINodeInfo feature gate must be enabled.
enable the VolumeSnapshotDataSource
Ğ’ĞºĞ»ÑÑ‡Ğ¸Ñ‚ÑŒ defaultstorageclass

0)Ğ£ÑÑ‚Ğ°Ğ½Ğ¾Ğ²Ğ¸Ñ‚ÑŒ csi-driver-host-path
https://github.com/kubernetes-csi/csi-driver-host-path
1) Ğ¡Ğ¾Ğ·Ğ´Ğ°Ñ‚ÑŒ hostpath CSI storage class
2) Ğ¡Ğ¾Ğ·Ğ´Ğ°Ñ‚ÑŒ hostpath CSI PVC(ÑÑƒÑ‰ĞµÑÑ‚Ğ²ÑƒÑÑ‰Ğ¸Ğ¹ PV Ñ‚Ğ¾Ğ¶Ğµ Ğ¼Ğ¾Ğ¶Ğ½Ğ¾ Ğ¸ÑĞ¿Ğ¾Ğ»ÑŒĞ·Ğ¾Ğ²Ğ°Ñ‚ÑŒ)
3) Ğ¡Ğ¾Ğ·Ğ´Ğ°Ñ‚ÑŒ pod Ñ hostpath CSI PVC
4) Ğ’ĞºĞ»ÑÑ‡Ğ¸Ñ‚ÑŒ Ğ½ĞµĞ¾Ğ±Ñ…Ğ¾Ğ´Ğ¸Ğ¼Ñ‹Ğµ Ğ¿Ğ»Ğ°Ğ³Ğ¸Ğ½Ñ‹ Ğ´Ğ»Ñ ÑĞ¾Ğ·Ğ´Ğ°Ğ½Ğ¸Ñ snapshots:
defaultStorageClass
VolumeSnapshotDataSource(alpha)
5) ĞĞ¿Ğ¸ÑĞ°Ñ‚ÑŒ Ğ¾Ğ±ÑŠĞµĞºÑ‚ Ñ‚Ğ¸Ğ¿Ğ¾ VolumeSnapshot(Ğ¿Ñ€Ğ¸ ÑƒĞºĞ°Ğ·Ğ°Ğ½Ğ¸Ğ¸ ÑÑ‚Ğ°Ğ½Ğ´Ğ°Ñ€Ñ‚Ğ½Ğ¾Ğ³Ğ¾ ĞºĞ»Ğ°ÑÑĞ° csi-hostpath-snapclass Ğ¾Ğ±ÑŠĞµĞºÑ‚ VolumeSnashotClass Ğ¼Ğ¾Ğ¶Ğ½Ğ¾ Ğ½Ğµ ÑĞ¾Ğ·Ğ´Ğ°Ğ²Ğ°Ñ‚ÑŒ)

sCN in PV = sCN in PVC
>>>>>>> 842117d1342c8b55ba959a84729b76fa46716365
