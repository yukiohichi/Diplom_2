#!/bin/bash

pytest --alluredir=allure-results
if [ $? -ne 0 ]; then
  echo "Ошибка: тесты не прошли или pytest завершился с ошибкой."
  exit 1
fi

allure generate allure-results --clean -o allure-report
if [ $? -ne 0 ]; then
  echo "Ошибка: не удалось сгенерировать отчет Allure."
  exit 1
fi


allure open allure-report
