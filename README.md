# pathfinder177_platform
homework-2

task-1
1) Создал ServiceAccount bob в первом манифесте
2) Создал ClusterRoleBinding на основе ClusterRole admin для subject bob во втором манифесте

task-2
1) Создал namespace prometheus в первом манифесте
2) Создал service account carol во втором манифесте
3) Создал ClusterRole pod-reader с verbs get, list,watch в третьем манифесте
4) Создал Rolebinding для subject groups, 
в котором определил system:serviceaccounts:prometheus для
делегирования роли pod-reader всем serviceaccounts в пределах namespace prometheus в четвертом манифесте

task-3
1) создал namespace dev
2) создал serviceaccount jane в namespace dev
3) Сделал Rolebinding для делегирования jane роли admin в namespace dev
4) создал serviceaccount ken в namespace dev
5) Сделал Rolebinding для делегирования ken роли view в namespace dev