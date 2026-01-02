/***************************************************
* Filename : ex07_if_elseif_else.c
* Description : ´Ü¼ø Á¶°Ç¹®
* Author	  : KHC
* History	  : 2025-12-31
*****************************************************/
# include <stdio.h>

void main() {
	// Â¦¼ö & È¦¼ö ÆÇº° Ãâ·Â
	int no = 7;
	char c = 'c';
	// »ïÇ× ¿¬»êÀÚ
	(no % 2) ? printf("%d - È¦¼ö\n", no) : printf("%d - Â¦¼ö\n", no);
	(c >= 'A' && c <= "Z") ? printf("%c - ´ë¹®ÀÚ",c) : (c >= 'a' && c <= 'z') ? printf("%c - ¼Ò¹®ÀÚ",c) : printf("¾ËÆÄºª ¾Æ´Ô",c);


}