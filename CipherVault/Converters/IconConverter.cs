using System;
using System.Globalization;
using System.Windows.Data;

namespace CipherVault.Converters
{
    public class IconConverter : IValueConverter
    {
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            if (value is string iconName)
            {
                switch (iconName)
                {
                    case "Pencil": return "\uE104"; // Edit / Pencil
                    case "Eye": return "\uE18B"; // Reveal / Eye
                    case "Hide": return "\uED1A"; // Hide
                    case "Copy": return "\uE8C8"; // Copy
                    case "Plus": return "\uE710"; // Add / Plus
                    default: return "\uE116"; // Default / Unknown (Document)
                }
            }
            return "\uE116"; // Default
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}
