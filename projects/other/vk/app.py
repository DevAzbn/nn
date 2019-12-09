# -*- coding: utf-8 -*-
import vk_api

cfg = {
	'vk' : {
		'app' : {
			'id' : 0,
			'key' : '',
			'skey' : '',
			'token' : '',
		},
	},
}

vk_session = vk_api.VkApi(token = cfg['vk']['app']['token'])
# vk_session.auth()
vk = vk_session.get_api()

# vk.wall.post(message = 'Hello, world!')
print(vk.account.getProfileInfo())