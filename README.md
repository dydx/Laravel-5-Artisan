Laravel 5 Artisan commands
===============

Fork of Sublime Text plugin for Laravel 4 Artisan commands

This plugin allows you the run the normal Artisan CLI using the Sublime Text interface, without having to open and use the command line.

Several of the commands, such as `Laravel Artisan: Make: Migration Schema` require `laracasts/generators` to be installed, as the associated commands are not native to Laravel (yet).

### Available commands:

##### General
- `Laravel Artisan: Clear Compiled`
- `Laravel Artisan: Down`
- `Laravel Artisan: Help`
- `Laravel Artisan: List`
- `Laravel Artisan: Migrate`
- `Laravel Artisan: Optimize`
- `Laravel Artisan: Serve`
- `Laravel Artisan: Up`

##### App
- `Laravel Artisan: App: Name`

##### Auth
- `Laravel Artisan: Auth: Clear Resets`

##### Cache
- `Laravel Artisan: Cache: Clear`
- `Laravel Artisan: Cache: Table`

##### Config
- `Laravel Artisan: Config: Cache`
- `Laravel Artisan: Config: Clear`

##### DB
- `Laravel Artisan: DB: Seed`

##### Event
- `Laravel Artisan: Event: Generate`

##### Key
- `Laravel Artisan: Key: Generate`

##### Make
- `Laravel Artisan: Make: Controller`
- `Laravel Artisan: Make: Event`
- `Laravel Artisan: Make: Middleware`
- `Laravel Artisan: Make: Migration`
- `Laravel Artisan: Make: Migration: Schema`
- `Laravel Artisan: Make: Migration: Pivot                  `
- `Laravel Artisan: Make: Model`
- `Laravel Artisan: Make: Provider`
- `Laravel Artisan: Make: Request`
- `Laravel Artisan: Make: Seeder`

##### Migrate
- `Laravel Artisan: Migrate: Install`
- `Laravel Artisan: Migrate: Refresh`
- `Laravel Artisan: Migrate: Reset`
- `Laravel Artisan: Migrate: Rollback`
- `Laravel Artisan: Migrate: Status`

##### Queue
- `Laravel Artisan: Queue: Failed`
- `Laravel Artisan: Queue: Failed: Table`
- `Laravel Artisan: Queue: Flush`
- `Laravel Artisan: Queue: Forget`
- `Laravel Artisan: Queue: Listen`
- `Laravel Artisan: Queue: Restart`
- `Laravel Artisan: Queue: Retry`
- `Laravel Artisan: Queue: Subscribe`
- `Laravel Artisan: Queue: Table`
- `Laravel Artisan: Queue: Work`

##### Route
- `Laravel Artisan: Route: Cache`
- `Laravel Artisan: Route: Clear`
- `Laravel Artisan: Route: List`

##### Schedule
- `Laravel Artisan: Schedule: Run`

##### Session
- `Laravel Artisan: Session: Table`

##### Vendor
- `Laravel Artisan: Vendor: Publish`

##### View
- `Laravel Artisan: View: Clear`

##### Custom
- `Laravel Artisan: Custom Command`

### Custom Commands
You can add custom commands.
Use `Preferences/Package Settings/Laravel 5 Artisan/Commands – User` menu item.

Simple command structure:

```json
[
    {
        "caption": "Laravel Artisan: Deploy Project",
        "command": "laravel5_artisan",
        "args": {
            "command": "deploy",
            "fill_in": true,
            "fill_in_lable": "Enter the branch name with options"
        }
    }
]
```

Change command `caption` and `command` in `args`.
Use `fill_in: true` if you need some input for your command and `fill_in_lable: "Text"` for message.

### Installation:
Use Package Controller or create a the directory `Laravel 5 Artisan` in your Sublime Text Packages directory with source code, and you're ready to go.

### Usage:
Press Cmd + Shift + P for the dropdown command list, search for `Laravel `, and pick your command. Also you can use `Tools/Laravel...` menu item

### Notes:
- Artisan file needs to been in the root folder of your structure in the sidebar.
- You need insert in Sublime Text user settings `"show_panel_on_build": true` or use `Tools/Build Results/Show Build Results` menu item for view results.
- Several commands do require [laracasts/generators](https://github.com/laracasts/Laravel-5-Generators-Extended) 
