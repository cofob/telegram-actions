<h1 align="center">:postbox: Telegram Actions for Github :postbox: </h1>

## Introduction
This is an action repository with an objective of notifying the user on Telegram regarding several changes in their github repositories. Messages sent to Telegram are rich-formatted, easy to read and comprehend and also contains supportive media to enhance the experience.

## Unique Features
1. Offers rich-formatted push messages with texts, emojis and all details regarding the event
2. Automatically adds the Github Avatar of the user who triggers the event in the message
3. Includes all relevant URLs for your quick review and launch them in Github app or website

## Get Started

### Configure your repository secrets
1. Navigate to your repository secrets ```Settings > Secrets```
2. Add below secrets using button ```New repository secret```

 Name              | Value                                              | 
-------------------|----------------------------------------------------|
BOT_TOKEN          | bot token from @botfather
BOT_CHAT_ID        | chat_id with this bot


### Prepare the action workflow
1. In your repository page, navigate to ```Actions > New Workflow > set up a workflow yourself```. It will open up a ```yaml``` file in code editor.
2. Replace everything in this ```yaml``` file with below:

```yaml
name: Telegram Notification

on: [push, pull_request, issues, fork, watch]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: telegram-notify
        uses: cofob/telegram-actions@main
        env:
          BOT_TOKEN: ${{ secrets.BOT_TOKEN }}
          BOT_CHAT_ID: ${{ secrets.BOT_CHAT_ID }}
```

## Screenshots

### Push

![](https://i.imgur.com/reQ9pFv.jpg)

### Watch

![](https://i.imgur.com/asZO7C5.jpg)

### Issue

![](https://i.imgur.com/QNl79kB.jpg)

## Support
Give us a :star2: to support!

Based on [this repo](https://github.com/kaviadigdarshan/whatsapp-actions) Copyright © 2021 [cofob](https://github.com/kaviadigdarshan)
