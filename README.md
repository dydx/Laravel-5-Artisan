Laravel 5 Artisan commands
===============

Fork of Sublime Text plugin for Laravel 4 Artisan commands

This plugin allows you the run the normal Artisan CLI using the Sublime Text interface, without having to open and use the command line.

Several of the commands, such as `Laravel Artisan: Make: Migration Schema` require `laracasts/generators` to be installed, as the associated commands are not native to Laravel (yet).

### Available commands:

##### General
- `Laravel Artisan 5: Clear Compiled`
- `Laravel Artisan 5: Down`
- `Laravel Artisan 5: Help`
- `Laravel Artisan 5: List`
- `Laravel Artisan 5: Migrate`
- `Laravel Artisan 5: Optimize`
- `Laravel Artisan 5: Serve`
- `Laravel Artisan 5: Up`

##### App
- `Laravel Artisan 5: App:Name`

##### Auth
- `Laravel Artisan 5: Auth:Clear Resets`

##### Cache
- `Laravel Artisan 5: Cache:Clear`
- `Laravel Artisan 5: Cache:Table`

##### Config
- `Laravel Artisan 5: Config:Cache`
- `Laravel Artisan 5: Config:Clear`

##### DB
- `Laravel Artisan 5: DB:Seed`

##### Event
- `Laravel Artisan 5: Event:Generate`

##### Key
- `Laravel Artisan 5: Key:Generate`

##### Make
- `Laravel Artisan 5: Make:Controller`
- `Laravel Artisan 5: Make:Event`
- `Laravel Artisan 5: Make:Middleware`
- `Laravel Artisan 5: Make:Migration`
- `Laravel Generate 5: Make:Migration: Schema`
- `Laravel Generate 5: Make:Migration: Pivot`
- `Laravel Artisan 5: Make:Model`
- `Laravel Artisan 5: Make:Provider`
- `Laravel Artisan 5: Make:Request`
- `Laravel Artisan 5: Make:Seeder`

##### Migrate
- `Laravel Artisan 5: Migrate:Install`
- `Laravel Artisan 5: Migrate:Refresh`
- `Laravel Artisan 5: Migrate:Reset`
- `Laravel Artisan 5: Migrate:Rollback`
- `Laravel Artisan 5: Migrate:Status`

##### Queue
- `Laravel Artisan 5: Queue:List Failed Jobs`
- `Laravel Artisan 5: Queue:Failed Table`
- `Laravel Artisan 5: Queue:Flush`
- `Laravel Artisan 5: Queue:Forget`
- `Laravel Artisan 5: Queue:Listen`
- `Laravel Artisan 5: Queue:Restart`
- `Laravel Artisan 5: Queue:Retry`
- `Laravel Artisan 5: Queue:Subscribe`
- `Laravel Artisan 5: Queue:Table`
- `Laravel Artisan 5: Queue:Work`

##### Route
- `Laravel Artisan 5: Route:Cache`
- `Laravel Artisan 5: Route:Clear`
- `Laravel Artisan 5: Route:List`

##### Schedule
- `Laravel Artisan 5: Schedule:Run`

##### Session
- `Laravel Artisan 5: Session:Table`

##### Vendor
- `Laravel Artisan 5: Vendor:Publish`

##### View
- `Laravel Artisan 5: View:Clear`

##### Custom
- `Laravel Artisan 5: Custom Command`

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
