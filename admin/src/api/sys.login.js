import request from '@/plugin/axios'

export function AccountLogin (auth) {
  return request({
    url: '/tokens',
    method: 'post',
    auth
  })
}
