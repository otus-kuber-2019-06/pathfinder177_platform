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