import time,json,requests,sys
from .config import Config
from .code_check import check

class Reward():

  def timestamp(self):
    time_stamp = int(time.time() * 1000)
    return time_stamp

  
  
  def reward_get(self,user_id,reward_code):
    host_timestamp = self.timestamp()
    id_search_url = f'{Config.MAIN_URL}{Config.ID_SEARCH}{Config.CALLBACK}=jQuery_{host_timestamp}&search_key={str(user_id)}&hostnum=10007&gameid=g83naxx2gb&type=uid&_={self.timestamp()}'
    data = requests.get(id_search_url).json()

    if data['status'] == True:
      status = '検索成功'
      nick = data['nick']
    elif data['status'] == False:
      status = '検索エラー'
      if data['code'] == 'UID_ERROR':
        print('そのIDを持つプレイヤーは居ませんでした')
        sys.exit()
      else:
        sys.exit()
        #Comming Soon
    
    print(f"{status}:{nick}")
    role_id = data['role_id']

    reward_get_url = f'{Config.MAIN_URL}{Config.REWARD_GET}{Config.CALLBACK}jQuery_{host_timestamp}&role_id={role_id}&hostnum=10007&code={str(reward_code)}&gameid=g83naxx2gb&_={self.timestamp()}'
    data = json.loads(requests.get(reward_get_url).text.split('(', 1)[1].rstrip(')'))
    status = data['status']

    #print(data)
    #デバッグ用

    if status == True:
      status = '有効'
      msg = Config.MSG200
    elif status == False:
      status = '無効'

    msg = check(data['code'])
    if msg == 'error':
      print('ーーーーーーーーーーーーーーー')
      print('↓この内容をコピーしてtwitter:@xc2p_に送信してください')
      print(f'ユーザーID:{user_id}')
      print(f'引き換えコード:{reward_code}')
      print(data)
      print('ーーーーーーーーーーーーーーー')
    print(f"コードステータス: {status}")
    print(f"{msg}")
