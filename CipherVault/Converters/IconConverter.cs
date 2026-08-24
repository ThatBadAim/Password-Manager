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
                    case "Pencil": return "\uE70F"; // Edit
                    case "Eye": return "\uE890"; // View
                    case "Copy": return "\uE8C8"; // Copy
                    case "Plus": return "\uE710"; // Add
                    default: return "\uE716"; // Dot / Default
                }
            }
            return "\uE716";
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}
