### Пример работы
Для запуска использовать `docker-compose up`
```
 ~nc localhost 5001
Hello
OK: Hello

Hello
Cached: Hello

Bye
OK: Bye

Bye
Cached: Bye

Bye
Cached: Bye

Hello
Cached: Hello

Mark
OK: Mark

Mark
Cached: Mark
```