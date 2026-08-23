using System;
using System.Globalization;
using System.Windows.Data;

namespace CipherVault.Converters
{
    public class IconConverter : IValueConverter
    {
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            if (value is string iconType)
            {
                return iconType switch
                {
                    "Pencil" => "\uE70F",
                    "Eye" => "\uE890",
                    "Copy" => "\uE8C8",
                    "Plus" => "\uE710",
                    _ => "\uE716" // Default dot or something
                };
            }
            return string.Empty;
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}
