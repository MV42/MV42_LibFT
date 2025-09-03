/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_degtorad.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: MV42                                       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/12/21 21:42:42 by MV42              #+#    #+#             */
/*   Updated: 2024/12/21 21:42:42 by MV42             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

// Converts degrees to radians.
// Multiplies degrees by pi/180 for the conversion.
// Uses 3.14159265358979323846 as the value of pi.
float	ft_degtorad(float deg)
{
	float		pi;
	float		rad;

	pi = 3.14159265358979323846f;
	rad = deg * (pi / 180.0f);
	return (rad);
}
