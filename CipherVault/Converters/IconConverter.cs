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
                return iconName switch
                {
                    "Pencil" => "\uE104",
                    "Eye" => "\uE18B",
                    "Copy" => "\uE8C8",
                    "Plus" => "\uE710",
                    _ => "\uE10C" // Default icon
                };
            }
            return "\uE10C";
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}
