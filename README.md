# MikroTik Scripts Collection

*[🇷🇺 Русская версия](README_ru.md)*

A comprehensive collection of scripts for automating MikroTik RouterOS device operations. Some scripts use SSH connection (port 22 should be open).

## 📋 Table of Contents

- [Script Descriptions](#-script-descriptions)
- [System Requirements](#-system-requirements)
- [Installation & Usage](#-installation--usage)
- [Configuration](#-configuration)
- [Security](#-security)
- [Contributing](#-contributing)
- [Support](#-support)
- [License](#-license)

## 🛠 Script Descriptions

### 🔐 Authentication & Security
- **RADIUS Server Authorization** - Centralized authentication setup via RADIUS server
- **Password Change Script** - Automated password rotation for enhanced security
- **IP Blocking Script** - Protection against brute-force attacks by blocking suspicious IPs
  > *Replace with your values for incoming interface, protocol, and port*

### 💾 Backup Solutions
- **Encrypted RouterOS Backup** - Secure configuration backup creation
- **Unencrypted RouterOS Backup** - Quick configuration backup creation
- **Encrypted RouterOS v7 Backup** - Support for newer RouterOS version 7
- **Automated Backup & Send** - Creates and sends backups via FTP automatically

### 📡 Monitoring & Notifications
- **User Login Monitoring** - Email notifications for user authentication on RouterOS
- **Dynamic IP Tracking** - Monitors public IP changes and sends email notifications
  > *Convenient for dynamic IP scenarios*
- **Host Availability Check** - Monitors network connectivity with automatic interface shutdown
  > *Checks host availability and disables specified interface if both primary and secondary hosts are unavailable*

## 🔧 System Requirements

- **RouterOS**: Version 6.x or 7.x (depending on script)
- **SSH Access**: Port 22 must be open for SSH-based scripts
- **Email Setup**: Configured SMTP server for notifications
- **FTP Server**: Configured FTP server for automated backups
- **Network Access**: Internet connectivity for monitoring scripts

## 🚀 Installation & Usage

### Method 1: Via Winbox
1. Download the required `.rsc` file
2. Open Winbox and connect to your router
3. Navigate to **Files** menu
4. Drag and drop the `.rsc` file into the window
5. Execute in terminal: `/import file-name.rsc`

### Method 2: Via Web Interface
1. Access RouterOS web interface
2. Navigate to **Files**
3. Click **Upload** and select the file
4. Execute in terminal: `/import file-name.rsc`

### Method 3: Via FTP
1. Enable FTP service on the router
2. Upload script via FTP client
3. Connect via terminal
4. Execute: `/import file-name.rsc`

### Method 4: Via SSH
1. Copy script content
2. Connect via SSH to your router
3. Paste and execute the script directly

## ⚙️ Configuration

### Variable Setup

Before using the scripts, replace the following values with your own:

```bash
# FTP Configuration (for backup scripts)
:local ftphost "192.168.1.2"          # FTP server IP address
:local ftpuser "ftp-user"              # FTP username
:local ftppassword "ftp-password"      # FTP password
:local ftppath "Mikrotik"              # FTP server path

# Email Configuration (for notifications)
:local emailserver "smtp.gmail.com"    # SMTP server
:local emailuser "your@email.com"      # Email username
:local emailpass "your-password"       # Email password
:local emailto "admin@company.com"     # Recipient email

# Monitoring Configuration
:local host1 "8.8.8.8"                # Primary host to check
:local host2 "1.1.1.1"                # Secondary host to check
:local interface "ether1"              # Interface to disable if hosts are down

# Security Configuration
:local srcInterface "ether1"           # Source interface for brute-force protection
:local protocol "tcp"                  # Protocol to monitor
:local port "22"                       # Port to monitor
```

### Scheduler Setup

For automatic script execution:

```bash
# Daily backup at 2:00 AM
/system scheduler add name="daily-backup" start-time="02:00:00" interval=1d \
on-event="/system script run backup-script"

# IP monitoring every hour
/system scheduler add name="ip-monitor" start-time="00:00:00" interval=1h \
on-event="/system script run ip-check"

# Brute-force protection check every 5 minutes
/system scheduler add name="security-check" start-time="00:00:00" interval=5m \
on-event="/system script run block-bruteforce"

# Host availability check every 2 minutes
/system scheduler add name="host-check" start-time="00:00:00" interval=2m \
on-event="/system script run host-availability"
```

## 🔒 Security

### Security Recommendations:
- Use strong passwords for FTP and email accounts
- Restrict SSH access to specific IP addresses only
- Regularly update RouterOS to latest stable version
- Store backups in secure, encrypted locations
- Use encrypted backups for critical configurations
- Monitor logs regularly for suspicious activities

### Firewall Configuration:
```bash
# Allow SSH only from specific IPs
/ip firewall filter add chain=input protocol=tcp dst-port=22 \
src-address=192.168.1.100 action=accept comment="Allow SSH from admin"

/ip firewall filter add chain=input protocol=tcp dst-port=22 \
action=drop comment="Block all other SSH"

# Create address list for blocked IPs
/ip firewall address-list add list="blocked-ips" address=0.0.0.0/1
/ip firewall filter add chain=input src-address-list="blocked-ips" \
action=drop comment="Drop blocked IPs"
```

### Best Practices:
- Test scripts in a lab environment before production deployment
- Create configuration backups before running new scripts
- Monitor system logs after script deployment
- Use least privilege principle for script permissions
- Document all customizations and modifications

## 📊 Script Performance

| Script Type | Execution Time | Resource Usage | Recommended Frequency |
|-------------|----------------|----------------|----------------------|
| Backup Scripts | 30-60 seconds | Low | Daily |
| Monitoring Scripts | 5-10 seconds | Very Low | Every 5-60 minutes |
| Security Scripts | 10-20 seconds | Low | Every 5-10 minutes |
| IP Tracking | 5-15 seconds | Very Low | Hourly |

## 🔧 Troubleshooting

### Common Issues:

**Problem**: Script import fails
**Solutions**:
- Check RouterOS version compatibility
- Verify script syntax
- Import in safe mode if needed
- Check available storage space

**Problem**: Email notifications not working
**Solutions**:
- Verify SMTP server settings
- Check email credentials
- Confirm network connectivity
- Review firewall rules for SMTP traffic

**Problem**: FTP backup fails
**Solutions**:
- Verify FTP server accessibility
- Check FTP credentials and permissions
- Ensure sufficient storage space
- Review network connectivity

**Problem**: SSH connection issues
**Solutions**:
- Verify SSH service is enabled
- Check firewall rules
- Confirm SSH port (default 22)
- Validate user permissions

## 📞 Support

If you encounter issues or have questions:

- **Create an issue** in the GitHub repository
- **Provide detailed description** of the problem
- **Include RouterOS version** and device model
- **Attach relevant logs** if possible
- **Mention steps to reproduce** the issue

## ⚠️ Disclaimer

- All scripts are provided "as is" without any warranties
- Test scripts in a safe environment before production use
- Author is not responsible for any damage caused by script usage
- Always create backups before making configuration changes
- Use scripts at your own risk

## 🔗 Useful Links

- [Official MikroTik Documentation](https://help.mikrotik.com/)
- [MikroTik Wiki](https://wiki.mikrotik.com/)
- [RouterOS Scripting Guide](https://help.mikrotik.com/docs/display/ROS/Scripting)
- [MikroTik Community Forum](https://forum.mikrotik.com/)
- [RouterOS Downloads](https://mikrotik.com/download)

## 📈 Version History

- **v1.0** - Initial collection of basic scripts
- **v1.1** - Added RouterOS v7 support
- **v1.2** - Enhanced security and monitoring features
- **v1.3** - Improved error handling and documentation

---

**⭐ If you find this project helpful, please give it a star!**