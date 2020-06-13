{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np #Импортируем библиотеку NumPy и сокращенно называем ее np.\n",
    "\n",
    "\n",
    "def game_core_v2(number):\n",
    "    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.\n",
    "       Функция принимает загаданное число и возвращает число попыток'''\n",
    "    count = 1\n",
    "    predict = np.random.randint(1,101)\n",
    "    while number != predict:\n",
    "        count+=1\n",
    "        if number > predict: \n",
    "            predict += 1\n",
    "        elif number < predict: \n",
    "            predict -= 1\n",
    "    return(count) # выход из цикла, если угадали\n",
    "\n",
    "def score_game(game_core):\n",
    "    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''\n",
    "    count_ls = []\n",
    "    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!\n",
    "    random_array = np.random.randint(1,101, size=1000)\n",
    "    for number in random_array:\n",
    "        count_ls.append(game_core(number))\n",
    "    score = int(np.mean(count_ls))\n",
    "    print(f\"Ваш алгоритм угадывает число в среднем за {score} попыток\")\n",
    "    return(score)\n",
    "\n",
    "game_core_v2(10)\n",
    "score_game(game_core_v2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "def game_core_v2(number):\n",
    "    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.\n",
    "       Функция принимает загаданное число и возвращает число попыток'''\n",
    "    count = 1\n",
    "    predict = np.random.randint(1,101)\n",
    "    while number != predict:\n",
    "        count+=1\n",
    "        if number > predict:\n",
    "            predict += 3\n",
    "        elif number < predict: \n",
    "            predict -= 3\n",
    "    return(count) # выход из цикла, если угадали\n",
    "\n",
    "game_core_v2(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ваш алгоритм угадывает число в среднем за 33 попыток\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "33"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np #Импортируем библиотеку NumPy и сокращенно называем ее np.\n",
    "\n",
    "\n",
    "def game_core_v2(number):\n",
    "    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.\n",
    "       Функция принимает загаданное число и возвращает число попыток'''\n",
    "    count = 1\n",
    "    predict = np.random.randint(1,101)\n",
    "    while number != predict:\n",
    "        count+=1\n",
    "        if number > predict: \n",
    "            predict += 1\n",
    "        elif number < predict: \n",
    "            predict -= 1\n",
    "    return(count) # выход из цикла, если угадали\n",
    "\n",
    "def score_game(game_core):\n",
    "    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''\n",
    "    count_ls = []\n",
    "    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!\n",
    "    random_array = np.random.randint(1,101, size=1000)\n",
    "    for number in random_array:\n",
    "        count_ls.append(game_core(number))\n",
    "    score = int(np.mean(count_ls))\n",
    "    print(f\"Ваш алгоритм угадывает число в среднем за {score} попыток\")\n",
    "    return(score)\n",
    "\n",
    "score_game(game_core_v2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ваш алгоритм угадывает число в среднем за 33 попыток\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "33"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np #Импортируем библиотеку NumPy и сокращенно называем ее np.\n",
    "\n",
    "def game_core_v2(number):\n",
    "    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.\n",
    "       Функция принимает загаданное число и возвращает число попыток'''\n",
    "    count = 1\n",
    "    predict = np.random.randint(1,101)\n",
    "    while number != predict:\n",
    "        count+=1 # увеличиваем счетчик числа попыток\n",
    "        if number > predict: \n",
    "            predict += 1\n",
    "        elif number < predict: \n",
    "            predict -= 1\n",
    "    return(count) # выход из цикла, если угадали\n",
    "\n",
    "def score_game(game_core):\n",
    "    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''\n",
    "    count_ls = []\n",
    "    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!\n",
    "    random_array = np.random.randint(1,101, size=1000)\n",
    "    for number in random_array:\n",
    "        count_ls.append(game_core(number))\n",
    "    score = int(np.mean(count_ls))\n",
    "    print(f\"Ваш алгоритм угадывает число в среднем за {score} попыток\")\n",
    "    return(score)\n",
    "\n",
    "score_game(game_core_v2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ваш алгоритм угадывает число в среднем за 33 попыток\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "33"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np #Импортируем библиотеку NumPy и сокращенно называем ее np.\n",
    "\n",
    "\n",
    "def game_core_v2(number):\n",
    "    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.\n",
    "       Функция принимает загаданное число и возвращает число попыток'''\n",
    "    count = 1\n",
    "    predict = np.random.randint(1,101)\n",
    "    while number != predict:\n",
    "        count+=1\n",
    "        if number > predict:\n",
    "            while predict > 15 and predict < 90:\n",
    "            if predict =< 50\n",
    "                predict += 10\n",
    "            else:\n",
    "                predict -= 25\n",
    "        elif number < predict: \n",
    "                predict -= 1\n",
    "    return(count) # выход из цикла, если угадали\n",
    "\n",
    "def score_game(game_core):\n",
    "    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''\n",
    "    count_ls = []\n",
    "    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!\n",
    "    random_array = np.random.randint(1,101, size=1000)\n",
    "    for number in random_array:\n",
    "        count_ls.append(game_core(number))\n",
    "    score = int(np.mean(count_ls))\n",
    "    print(f\"Ваш алгоритм угадывает число в среднем за {score} попыток\")\n",
    "    return(score)\n",
    "\n",
    "score_game(game_core_v2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np #Импортируем библиотеку NumPy и сокращенно называем ее np.\n",
    "\n",
    "\n",
    "def game_core_v2(number):\n",
    "    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.\n",
    "       Функция принимает загаданное число и возвращает число попыток'''\n",
    "    count = 1\n",
    "    predict = 50\n",
    "    while number != predict:\n",
    "        count+=1\n",
    "        if number > predict: # если загаднное число больше 50\n",
    "            predict += 25 # увеличиваем наше число на половину от первоначального - до 75.\n",
    "            if number > predict: # загаданное число больше 75\n",
    "                predict += 12 # увеличиваем наше число 75 на 12 - до 87\n",
    "                if number > predict: # если загаданное число больше 87 - прибавляем по одному\n",
    "                    predict += 1\n",
    "                else:                # если загаданное число меньше 87 - отнимаем по одному\n",
    "                    predict -= 1\n",
    "            else:              # загаданное число меньше 75\n",
    "                predict -= 12  # уменьшаем наше число 75 на 12 - до 63\n",
    "                if number > predict: # если загаданное число больше 63 - прибавляем по одному\n",
    "                    predict += 1\n",
    "                else:                # если загаданное число меньше 63 - отнимаем по одному\n",
    "                    predict -= 1\n",
    "                    \n",
    "        elif number < predict: # если загаднное число меньше 50\n",
    "            predict -= 25 # уменьшаем наше число на половину от первоначального - до 25.\n",
    "            if number < predict: # загаданное число меньше 25\n",
    "                predict -= 12  # уменьшаем наше число 25 на 12 - до 13\n",
    "                 number > predict:\n",
    "                    predict += 1\n",
    "                else:\n",
    "                    predict -= 1\n",
    "            else:                # загаданное число больше 25\n",
    "                predict += 12  # увеличиваем наше число 25 на 12 - до 37\n",
    "                if number > predict: # если загаданное число больше 37 - прибавляем по одному\n",
    "                    predict += 1\n",
    "                else:                # если загаданное число меньше 37 - отнимаем по одному\n",
    "                    predict -= 1\n",
    "    return(count) # выход из цикла, если угадали\n",
    "\n",
    "def score_game(game_core):\n",
    "    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''\n",
    "    count_ls = []\n",
    "    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!\n",
    "    random_array = np.random.randint(1,101, size=1000)\n",
    "    for number in random_array:\n",
    "        count_ls.append(game_core(number))\n",
    "    score = int(np.mean(count_ls))\n",
    "    print(f\"Ваш алгоритм угадывает число в среднем за {score} попыток\")\n",
    "    return(score)\n",
    "\n",
    "score_game(game_core_v2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ваш алгоритм угадывает число в среднем за 5 попыток\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np #Импортируем библиотеку NumPy и сокращенно называем ее np.\n",
    "import random\n",
    "\n",
    "def game_core_v2(number):\n",
    "    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.\n",
    "        Функция принимает загаданное число и возвращает число попыток'''\n",
    "    count = 1\n",
    "    predict = 50\n",
    "    n = predict\n",
    "\n",
    "    while number != predict:\n",
    "        \n",
    "        count += 1\n",
    "        if n > 1:\n",
    "          n = n // 2\n",
    "        \n",
    "        if predict < number:\n",
    "            predict += int(n)\n",
    "\n",
    "        elif predict > number:\n",
    "            predict -= int(n)\n",
    "\n",
    "    return count # выход из цикла, если угадали\n",
    "        \n",
    "\n",
    "def score_game(game_core):\n",
    "    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''\n",
    "    count_ls = []\n",
    "    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!\n",
    "    random_array = np.random.randint(1,101, size=1000)\n",
    "    for number in random_array:\n",
    "        count_ls.append(game_core(number))\n",
    "    score = int(np.mean(count_ls))\n",
    "    print(f\"Ваш алгоритм угадывает число в среднем за {score} попыток\")\n",
    "    return(score)\n",
    "\n",
    "score_game(game_core_v2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ваш алгоритм угадывает число в среднем за 1 попыток\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np #Импортируем библиотеку NumPy и сокращенно называем ее np.\n",
    "\n",
    "\n",
    "def game_core_v2(number):\n",
    "    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.\n",
    "       Функция принимает загаданное число и возвращает число попыток'''\n",
    "    count = 1\n",
    "    predict = 50\n",
    "    while number != predict:\n",
    "        count+=1\n",
    "        if number > predict: # если загаданное число больше 50\n",
    "            predict += 25 # увеличиваем наше число на половину от первоначального - до 75.\n",
    "            if number > predict: # загаданное число больше 75\n",
    "                predict += 12 # увеличиваем наше число 75 на 12 - до 87\n",
    "                while number != predict:\n",
    "                    if number > predict: # если загаданное число больше 87 - прибавляем по одному\n",
    "                        predict += 1\n",
    "                    else:                # если загаданное число меньше 87 - отнимаем по одному\n",
    "                        predict -= 1\n",
    "            else:              # загаданное число меньше 75\n",
    "                predict -= 12  # уменьшаем наше число 75 на 12 - до 63\n",
    "                while number != predict:\n",
    "                    if number > predict: # если загаданное число больше 63 - прибавляем по одному\n",
    "                        predict += 1\n",
    "                    else:                # если загаданное число меньше 63 - отнимаем по одному\n",
    "                        predict -= 1\n",
    "                    \n",
    "        elif number < predict: # если загаданное число меньше 50\n",
    "            predict -= 25 # уменьшаем наше число на половину от первоначального - до 25.\n",
    "            if number < predict: # загаданное число меньше 25\n",
    "                predict -= 12  # уменьшаем наше число 25 на 12 - до 13\n",
    "                while number != predict:\n",
    "                    if number > predict:\n",
    "                        predict += 1\n",
    "                    else:\n",
    "                        predict -= 1\n",
    "            else:                # загаданное число больше 25\n",
    "                predict += 12  # увеличиваем наше число 25 на 12 - до 37\n",
    "                while number != predict:\n",
    "                    if number > predict: # если загаданное число больше 37 - прибавляем по одному\n",
    "                        predict += 1\n",
    "                    else:                # если загаданное число меньше 37 - отнимаем по одному\n",
    "                        predict -= 1\n",
    "    return(count) # выход из цикла, если угадали\n",
    "\n",
    "def score_game(game_core):\n",
    "    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''\n",
    "    count_ls = []\n",
    "    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!\n",
    "    random_array = np.random.randint(1,101, size=1000)\n",
    "    for number in random_array:\n",
    "        count_ls.append(game_core(number))\n",
    "    score = int(np.mean(count_ls))\n",
    "    print(f\"Ваш алгоритм угадывает число в среднем за {score} попыток\")\n",
    "    return(score)\n",
    "\n",
    "score_game(game_core_v2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "14"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np #Импортируем библиотеку NumPy и сокращенно называем ее np.\n",
    "\n",
    "\n",
    "def game_core_v2(number):\n",
    "    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.\n",
    "       Функция принимает загаданное число и возвращает число попыток'''\n",
    "    count = 1\n",
    "    predict = 50\n",
    "    while number != predict:\n",
    "        count+=1\n",
    "        if number > predict: # если загаданное число больше 50\n",
    "            predict += 25 # увеличиваем наше число на половину от первоначального - до 75.\n",
    "            if number > predict: # загаданное число больше 75\n",
    "                predict += 12 # увеличиваем наше число 75 на 12 - до 87\n",
    "                while number != predict:\n",
    "                    count+=1\n",
    "                    if number > predict: # если загаданное число больше 87 - прибавляем по одному\n",
    "                        predict += 1\n",
    "                    else:                # если загаданное число меньше 87 - отнимаем по одному\n",
    "                        predict -= 1\n",
    "            else:              # загаданное число меньше 75\n",
    "                predict -= 12  # уменьшаем наше число 75 на 12 - до 63\n",
    "                while number != predict:\n",
    "                    count+=1\n",
    "                    if number > predict: # если загаданное число больше 63 - прибавляем по одному\n",
    "                        predict += 1\n",
    "                    else:                # если загаданное число меньше 63 - отнимаем по одному\n",
    "                        predict -= 1\n",
    "\n",
    "        elif number < predict: # если загаданное число меньше 50\n",
    "            predict -= 25 # уменьшаем наше число на половину от первоначального - до 25.\n",
    "            if number < predict: # загаданное число меньше 25\n",
    "                predict -= 12  # уменьшаем наше число 25 на 12 - до 13\n",
    "                while number != predict:\n",
    "                    count+=1\n",
    "                    if number > predict:\n",
    "                        predict += 1\n",
    "                    else:\n",
    "                        predict -= 1\n",
    "            else:                # загаданное число больше 25\n",
    "                predict += 12  # увеличиваем наше число 25 на 12 - до 37\n",
    "                while number != predict:\n",
    "                    count+=1\n",
    "                    if number > predict: # если загаданное число больше 37 - прибавляем по одному\n",
    "                        predict += 1\n",
    "                    else:                # если загаданное число меньше 37 - отнимаем по одному\n",
    "                        predict -= 1\n",
    "        \n",
    "    return(count) # выход из цикла, если угадали\n",
    "\n",
    "game_core_v2(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ваш алгоритм угадывает число в среднем за 5 попыток\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def game_core_v2(number):\n",
    "    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.\n",
    "       Функция принимает загаданное число и возвращает число попыток'''\n",
    "    count = 1\n",
    "    predict = 50\n",
    "    n = predict             # Вводим дополнительную переменную, равную заданному нами числу и над которой будут совершаться действия \n",
    "                            # по получению половины от заданного нами числа.\n",
    "    while number != predict:\n",
    "        count+=1\n",
    "        \n",
    "        if n > 1:            \n",
    "            n = int(n//2)   # Делим заданное нами число нацело на два.\n",
    "         \n",
    "        if number > predict: \n",
    "            predict += n    # Если загаданное число больше заданного, то прибавляем половину от заданного к заданному\n",
    "                            # нами числу.\n",
    "        elif number < predict: \n",
    "            predict -= n    # Если загаданное число меньше заданного, то от заданного числа отнимаем его половину.\n",
    "    return(count) # выход из цикла, если угадали\n",
    "\n",
    "\n",
    "def score_game(game_core):\n",
    "    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''\n",
    "    count_ls = []\n",
    "    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!\n",
    "    random_array = np.random.randint(1,101, size=(1000))\n",
    "    for number in random_array:\n",
    "        count_ls.append(game_core(number))\n",
    "    score = int(np.mean(count_ls))\n",
    "    print(f\"Ваш алгоритм угадывает число в среднем за {score} попыток\")\n",
    "    return(score)\n",
    "\n",
    "score_game(game_core_v2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def game_core_v2(number):\n",
    "    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.\n",
    "       Функция принимает загаданное число и возвращает число попыток'''\n",
    "    count = 1\n",
    "    predict = 50\n",
    "    n = predict\n",
    "    \n",
    "    while number != predict:\n",
    "        count+=1\n",
    "        \n",
    "        if n >= 1:\n",
    "            n = int(n//2)\n",
    "         \n",
    "        if number > predict: \n",
    "            predict += n\n",
    "        elif number < predict: \n",
    "            predict -= n\n",
    "    return(count) # выход из цикла, если угадали\n",
    "\n",
    "game_core_v2(13)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def game_core_v2(number):\n",
    "    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.\n",
    "        Функция принимает загаданное число и возвращает число попыток'''\n",
    "    count = 1\n",
    "    predict = 50\n",
    "    n = predict\n",
    "\n",
    "    while number != predict:\n",
    "        \n",
    "        count += 1\n",
    "        if n > 1:\n",
    "          n = n // 2\n",
    "        \n",
    "        if predict < number:\n",
    "            predict += int(n)\n",
    "\n",
    "        elif predict > number:\n",
    "            predict -= int(n)\n",
    "\n",
    "    return count # выход из цикла, если угадали"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
