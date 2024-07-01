def check(code):
  if code == 'CODE_EROOR':
    return '交換コードが無効です'
  elif code == 'REDEEMED_ALREADY':
    return 'すでに同一タイプのアイテムを交換済みです'
  elif code == 'JIFEI_ERROR':
    return 'この引き換えコードの使用回数が上限に達しています。その他の公式イベントにもご注目ください。'
  elif code == 'TIME_ERROR':
    return '引き換え期間を過ぎたため、ギフトコードの引き換えはできません。必ず期間内に引き換えしてください'
  else:
    return 'error'