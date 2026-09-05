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
                    "Pencil" => "\xE70F",
                    "Eye" => "\xE890",
                    "Copy" => "\xE8C8",
                    "Plus" => "\xE710",
                    _ => ""
                };
            }
            return "";
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}
