<?php
//1
$cities = [
    "Москва",
    "Санкт-Петербург",
    "Казань",
    "Сочи",
    "Владивосток"
];

echo $cities[0] . "<br>";
echo $cities[2] . "<br>";
echo $cities[4] . "<br>";



//2
$numbers = [10, 20, 30, 40];

$numbers[1] = 200;

$numbers[] = 50;

$numbers[] = 60;

foreach ($numbers as $number) {
    echo $number . "<br>";
}


//3
$products = [
    "Ноутбук",
    "Мышь",
    "Клавиатура",
    "Монитор",
    "Наушники"
];

echo "Количество товаров: " . count($products) . "<br><br>";

foreach ($products as $product) {
    echo $product . "<br>";
}



//4
$numbers = [12, 7, 24, 15, 8, 31, 40, 55];

foreach ($numbers as $number) {
    if ($number % 2 == 0) {
        echo $number . "<br>";
    }
}



//5
$names = [
    "Иван",
    "Анна",
    "Пётр",
    "Мария",
    "Алексей"
];

$name = readline("Введите имя: ");

if (in_array($name, $names)) {
    echo "Пользователь найден";
} else {
    echo "Пользователь не найден";
}




//6
$numbers = [45, 12, 78, 3, 25, 9, 100];

print_r($numbers);

sort($numbers);

echo "<br>По возрастанию:<br>";
print_r($numbers);

rsort($numbers);

echo "<br>По убыванию:<br>";
print_r($numbers);




//7
$names = [
    "Иван",
    "Пётр",
    "Анна",
    "Мария"
];

array_pop($names);

array_unshift($names, "Алексей");

array_shift($names);

print_r($names);




//8
$user = [
    "name" => "Иван",
    "age" => 20,
    "email" => "ivan@mail.ru",
    "city" => "Москва"
];

echo "Имя: " . $user["name"] . "<br>";

echo "Возраст: " . $user["age"] . "<br>";

echo "Город: " . $user["city"] . "<br>";

$user["age"] = 21;

$user["phone"] = "+79991234567";

echo "<br>Все данные:<br>";

foreach ($user as $key => $value) {
    echo $key . ": " . $value . "<br>";
}




//9
$users = [
    [
        "name" => "Иван",
        "age" => 20
    ],
    [
        "name" => "Анна",
        "age" => 17
    ],
    [
        "name" => "Пётр",
        "age" => 25
    ],
    [
        "name" => "Мария",
        "age" => 16
    ],
    [
        "name" => "Алексей",
        "age" => 30
    ]
];

echo "Все пользователи:<br>";

foreach ($users as $user) {
    echo $user["name"] . " — " . $user["age"] . " лет<br>";
}

echo "<br>Совершеннолетние:<br>";

foreach ($users as $user) {
    if ($user["age"] >= 18) {
        echo $user["name"] . "<br>";
    }
}

echo "<br>Несовершеннолетние:<br>";

foreach ($users as $user) {
    if ($user["age"] < 18) {
        echo $user["name"] . "<br>";
    }
}

echo "<br>Количество пользователей: " . count($users);




//10
$products = [
    [
        "name" => "Ноутбук",
        "price" => 70000
    ],
    [
        "name" => "Мышь",
        "price" => 1500
    ],
    [
        "name" => "Клавиатура",
        "price" => 3000
    ],
    [
        "name" => "Монитор",
        "price" => 25000
    ]
];

echo "Все товары:<br>";

foreach ($products as $product) {
    echo $product["name"] . " — " . $product["price"] . " руб.<br>";
}

echo "<br>Товары дороже 5000:<br>";

foreach ($products as $product) {
    if ($product["price"] > 5000) {
        echo $product["name"] . "<br>";
    }
}

$total = 0;

foreach ($products as $product) {
    $total += $product["price"];
}

echo "<br>Общая стоимость: " . $total . " руб.<br>";

$expensive = $products[0];

foreach ($products as $product) {
    if ($product["price"] > $expensive["price"]) {
        $expensive = $product;
    }
}

echo "Самый дорогой товар: " . $expensive["name"] . " — " . $expensive["price"] . " руб.";
?>