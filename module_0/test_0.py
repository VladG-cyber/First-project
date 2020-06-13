{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
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
