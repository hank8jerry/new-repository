import discord
from discord.ext import commands

# 設定機器人的 intents
intents = discord.Intents.default()
intents.messages = True  # 啟用接收消息的事件
intents.message_content = True  # 啟用接收消息內容（需要在 Discord 開發者門戶中啟用特權 intents）

# 創建機器人對象
bot = commands.Bot(command_prefix='/', intents=intents)

# 當機器人啟動時觸發
@bot.event
async def on_ready():
    print(f'已登入為 {bot.user}')

# 定義 /math 指令
@bot.command()
async def math(ctx, *, expression: str):
    try:
        # 安全地計算數學表達式
        result = eval(expression, {"__builtins__": None}, {})
        await ctx.send(f'答案: {result}')
    except Exception as e:
        await ctx.send('無法計算，請檢查算式是否正確！')

# 請替換為你的機器人 Token
bot.run('1d4955dd2c4ec44d90fe00b3da4d3dae')