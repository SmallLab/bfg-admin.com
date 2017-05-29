var my_ajax_req ={ // создаем экземпляр объекта

// задаем свойства объекта
    updInterval: 10000, // 10 сек. - интервал времени между запросами
    url: 'ajax.php', // скрипт который должен отвечать на Ajax запросы
    init: function(){
        var self = my_ajax_req;
        setInterval($.proxy(my_ajax_req.requestData, self), self.updInterval);
    },

    requestData: function(){
        var self = my_ajax_req;

        // ajax запрос посредством JQuery
        $.ajax({
            url: self.url,
            type: 'GET',
            dataType: 'json',
            success: function(data){ self.update(data) },
            error: function(data){ self.error(data) },
        });
    },

    // метод принимает ответ на Ajax запрос
    update: function(Data){
        var self = my_ajax_req;
        console.log(Data);
        // тут можно дописать логику после получения данных
    },

    // метод для обработки ошибок
    error: function(Data){
        var self = my_ajax_req;
        console.log('Failed to get data');
    },
}
