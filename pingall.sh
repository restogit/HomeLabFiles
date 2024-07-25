# bash script to ping gns3 devices
# script is saved in the Network Automation device
# need to change the for-loop for a range of IP addresses
# so I don't have to type them all

IP_ADDRESSES=("ip-address-here" "next-IP-address-here") # Replace with your desired IP addresses in quotes, separated by a space
COUNT=1 # Number of ping attempts
 
for IP in "${IP_ADDRESSES[@]}"; do
  if ping -c $COUNT $IP > /dev/null 2>&1; then
    echo "Ping to $IP was successful."
  else
    echo "Ping to $IP failed."
  fi
done
