$VMSuffix =@(1..5) <# How many VMs you want to create #>

Foreach ($VM in $VMSuffix) 
{ 
$DiskNo = $VM <# To add same no. of physical disk to the VM #>

$VMName = "SampleVM"+$VM <# Setting up the VM name #>

try {

$ErrorActionPreference = "Stop"

#New-VHD -ParentPath "F:\VMC_GOLDEN_WIN10.vhdx" -Differencing -Path "F:\$VMName.vhdx" <# To use an existing VHDX as Golden VHDX template to make use of already installed OS #>

New-VHD -Path "F:\$VMName.vhdx" -SizeBytes 40GB -Dynamic <# To create a new VHDX and install OS later #>

New-VM -VHDPath "F:\$VMName.vhdx" -VMName $VMName -MemoryStartupBytes 4GB -Generation 1 <# Creating the VM #>

Add-VMNetworkAdapter -VMName $VMName -SwitchName "VM-Network old" -Name "VM-Network old" <# Configuring the Network Adapter settings#>

Set-VMProcessor -VMName $VMName -Count 2 <# How many virtual processors you want to assign to the VM #>

Get-VMScsiController –VMName $VMName | Add-VMHardDiskDrive –DiskNumber $DiskNo  <# Adding the external physical disk to the VM to run IOs on #>

Start-VM -Name $VMName <#Starting the VM #>


}

catch {
 
 If($($_.Exception.Message) -eq "The operation cannot be performed while the object is in use." )
 {
  
  "The Physical Disk $DiskNo you tried to attach to the VM $VMName is already in use, kindly free it up, do cleanup (Delete $VMName and F:\$VMName.vhdx) and re-run the script."
 }
 
 Elseif($($_.Exception.Message) -match "Failed to create the virtual hard disk." )
 {

  "F:\$VMName.vhdx is in use already, kindly delete it and re-run the script. "

 }
}
}