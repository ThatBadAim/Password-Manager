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
                    case "Pencil":
                        return "\xE70F"; // Edit icon
                    case "Eye":
                        return "\xE890"; // HideBcc/Eye icon
                    case "Copy":
                        return "\xE8C8"; // Copy icon
                    case "Plus":
                        return "\xE710"; // Add icon
                    default:
                        return "\xE783"; // Default icon
                }
            }
            return "\xE783"; // Default icon
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}
