#include <linux/module.h>
#define INCLUDE_VERMAGIC
#include <linux/build-salt.h>
#include <linux/elfnote-lto.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;
BUILD_LTO_INFO;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(".gnu.linkonce.this_module") = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif

static const struct modversion_info ____versions[]
__used __section("__versions") = {
	{ 0x2f1b9ab7, "module_layout" },
	{ 0xac8a34c0, "cdev_del" },
	{ 0x2701001f, "pci_unregister_driver" },
	{ 0x6bc3fbc0, "__unregister_chrdev" },
	{ 0xb50c5cd2, "class_destroy" },
	{ 0x2dd28857, "device_destroy" },
	{ 0xf3e3260, "cdev_add" },
	{ 0xf234a22a, "device_create" },
	{ 0xad3b86f0, "cdev_init" },
	{ 0x827ba31, "__class_create" },
	{ 0xe3ec2f2b, "alloc_chrdev_region" },
	{ 0xf678ed27, "__pci_register_driver" },
	{ 0xc959d152, "__stack_chk_fail" },
	{ 0xde80cd09, "ioremap" },
	{ 0x14afb8c4, "pci_read_config_dword" },
	{ 0x97df260b, "pci_read_config_byte" },
	{ 0x2318fa3, "pci_enable_device" },
	{ 0x686a28d9, "pci_disable_device" },
	{ 0xedc03953, "iounmap" },
	{ 0x6b10bee1, "_copy_to_user" },
	{ 0xa78af5f3, "ioread32" },
	{ 0x4a453f53, "iowrite32" },
	{ 0x13c49cc2, "_copy_from_user" },
	{ 0x88db9f48, "__check_object_size" },
	{ 0xc5850110, "printk" },
	{ 0xbdfb6dbb, "__fentry__" },
};

MODULE_INFO(depends, "");

MODULE_ALIAS("pci:v00001172d00000004sv*sd*bc*sc*i*");

MODULE_INFO(srcversion, "47F2EB9651C192828126682");
