import asyncio
import simpleobsws

#OBS Configs. (match scene, host, port and pasword)
async def create_dice_source(roll, scene_name = 'Screen' , host='127.0.0.1', port=4444, password='rolldice', loop=None): #<--- Download WebSockets plugin on OBS and change your configs here.
    if loop is None:
        loop = asyncio.get_event_loop()

    #Connect from OBS
    ws = simpleobsws.obsws(host=host, port=port, password=password, loop=loop)
    await ws.connect()

    try:
        #Create browser source in OBS scene
        await ws.call(
            'CreateSource', {
                'sourceName': 'DiceBot',
                'sourceKind': 'browser_source',
                'sceneName': scene_name,
                'setVisible': True
            }
        )
        #Settings source
        await ws.call(
            'SetSourceSettings', {
                'sourceName': 'DiceBot',
                'sourceSettings': {
                    'css': '',
                    'height': 1080,  # <--- change source resolution
                    'width': 1920,  # <--- change source resolution
                    'shutdown': True,
                    'url': 'http://dice.bee.ac/?noresult&dicehex=722f37&labelhex=ffffff&chromahex=00ff00&roll&d='+roll #urldice: resultbghex=fafafa&resulthex=0e1111&
                    #Can be changed in 'http://dice.bee.ac/' website

                }
            }
        )
        #Chroma key added to the source
        await ws.call(
            'AddFilterToSource', {
                'sourceName': 'DiceBot',
                'filterName': 'Chroma Key',
                'filterType': 'chroma_key_filter',
                'filterSettings': {}
            }
        )
        #How long will the source exist
        await asyncio.sleep(6)
        #Delete the source from the scene
        await ws.call(
            'DeleteSceneItem', {
                'scene': scene_name,
                'item': {
                    'name': 'DiceBot'
                    }
                }
            )
    finally:
        #Disconnect from OBS
        await ws.disconnect()
