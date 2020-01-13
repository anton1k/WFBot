# Telegram bot

## Telegram bot принимает ник персонажа игрока Warface, и возврашает: ранг, ник, стату, проведенное время время в игре, любимый класс PVP, любимый класс PVE, всего боев PVP, количество побед PVP, количество поражений PVP, всего миссий PVE, пройдено миссий PVE, провалено миссий PVE

### deploy on the heroku

>heroku login
>heroku create
>git init
>heroku git:remote -a name
>git add .    
>git commit -am "make it better" 
>git push heroku master    
>heroku ps:scale bot=1 
>heroku logs - если нужно
>
>heroku ps:stop bot - отключаем бота