var tg = window.Telegram.WebApp;

// Расширяем на весь экран.
tg.expand();

// Кнопка просмотра заказа (реализуется тг - не сайтом).
tg.MainButton.textColor = '#FFFFFF';
tg.MainButton.color = '#2cab37';

// Хранение выбранного товара.
let item = "";

let prices = new Object();
prices[1] = 220;
prices[2] = 460;
prices[3] = 240;
prices[4] = 190;
prices[5] = 100;
prices[6] = 150;

for (var i = 1; i <= 6; i++) {
	let btn = document.getElementById("btn" + i.toString());
	btn.btn_id = i;
	btn.price = prices[i];
	btn.addEventListener("click", function() {
		if (tg.MainButton.isVisible) {
			tg.MainButton.hide();
		}
		else {
			tg.MainButton.setText("Перейти к оплате (" + btn.price.toString() + "₽)");
			item = this.btn_id.toString();
			tg.MainButton.show();
		}
	});
}

// Отправка данных в тг.
Telegram.WebApp.onEvent("mainButtonClicked", function(){
	tg.sendData(item);
});

// Добавление в usercard данных из тг.
let usercard = document.getElementById("usercard");

let p = document.createElement("p");

p.innerText = `${tg.initDataUnsafe.user.first_name}
${tg.initDataUnsafe.user.last_name}`;

usercard.appendChild(p);