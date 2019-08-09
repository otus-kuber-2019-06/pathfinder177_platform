homework-4
Kubernetes-volumes

1. Решил проблему с невозможность pull images via kind - включил ipv4.forwarding на node
2. Применил манифест с minio
3. Все соответствующие ресурсы были созданы - pod, pvc, pv с помощью storage class
4. При попытке удалить pod minio-0 StatefulSet Controller пересоздает его
5. Применил манифест с headless service. Можно было бы специфицировать ресурсы для приложения
6. В контейнере с kind создался headless сервис с внутренним ip-address
7. При попытке сделать curl по :9000 - access denied, состояние системы=желаемому состоянию
8. Со * - создал секрет с текстовыми данными для minio(доступны как переменные из контейнера), специфицировал
секрет для использования в minio-statefulset.yaml