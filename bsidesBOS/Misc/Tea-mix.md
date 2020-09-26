
# Tea-mix
The name hinted towards tmux, which was confirmed by session files for tmux in /tmp; including /tmp/tmux-0/tea_mix (root's session) 
We have permission toy read the socket file, meaning we can attach to the tmux session.
```
export TERM=xterm
set tty rows/cols to your own terminal
tmux -S /tmp/tmux-0/tea_mix
root shell
cat /root/flag.txt
```
#### Flag: flag{oooohhhh_tea_mix_sounds_like_tmux_i_get_it}
