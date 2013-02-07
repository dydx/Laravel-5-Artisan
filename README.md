sublime-artisan
===============

Sublime Text plugin for Laravel Artisan commands

This plugin allows you the run the normal Artisan CLI using the Sublime Text interface, without having to open and use the command line.

Options Available:
- Help (php artisan help:commands)
- Generate an application key (php artisan key:generate)
- Create a session table (php artisan session:table)
- Create the Laravel migration table (php artisan migrate:install)
- Creating a migration	(php artisan migrate:make create_users_table)
- Creating a migration for a bundle	(php artisan migrate:make bundle::tablename)
- Running outstanding migrations (php artisan migrate)
- Running outstanding migrations in the application	(php artisan migrate application)
- Running all outstanding migrations in a bundle (php artisan migrate bundle)
- Rolling back the last migration operation	(php artisan migrate:rollback)
- Roll back all migrations that have ever run (php artisan migrate:reset)
- Install a bundle (php artisan bundle:install eloquent)
- Upgrade a bundle (php artisan bundle:upgrade eloquent)
- Upgrade all bundles	(php artisan bundle:upgrade)
- Publish a bundle assets (php artisan bundle:publish bundle_name)
- Publish all bundles assets (php artisan bundle:publish)
- Calling a task (php artisan notify), or passing arguments (php artisan notify taylor)
- Running the application tests (php artisan test)
- Running the bundle tests (php artisan test bundle-name)
- Calling a route (php artisan route:call get api/user/1)
