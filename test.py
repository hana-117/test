import PySimpleGUI as sg

layout = [
    [sg.Button('ポップアップを表示',key = '-BTN-')]
]

window = sg.Window('ボタンにイベントを追加', layout, size=(300, 100))

while True:
    event, value = window.read()  # イベントの入力を待つ
    print('a')
    print('b')
    print('c')
    print('テストブランチ作成')
    print('2回目のコミット')

    if event == '-BTN-':
        sg.popup('ボタンが押されました')
        break
    elif event is None:
        break

window.close()