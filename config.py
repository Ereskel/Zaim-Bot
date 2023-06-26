from environs import Env

env = Env()
env.read_env()

token = env.str('token')
admins = env.list('admins')

channel1 = '@ttttxtxer'
channel2 = '@kkkkkkaktr'