from aiogram import Bot, Dispatcher, executor, types
import python_weather

#bot init
bot = Bot(token="6127109129:AAFNWUbFTjZrTB5aYqkJZ7I6OLxIXxOSzj8")
dp = Dispatcher(bot)
client = python_weather.Client(format=python_weather.METRIC)
      
#echo
@dp.message_handler()
async def echo(message: types.Message):
    weather = await client.get(message.text)
    
    weather.current.tempereture = popka

    resp_msg = f"Текущая температура: {round(weather.current.temperature)} °С\n"
    
    if popka < 15:
     resp_msg += "\n\nВооу, довольно прохладно, надеваем кофточки!' "
    
    elif popka < 0:
     resp_msg += "\n\nМорозно, чел, в лужу не встрянешь! :)"
     
    else:
      resp_msg += "\n\nУх, жарааааааа!!!"
    
    await message.answer(resp_msg)

#run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
